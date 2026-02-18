<?php

namespace App\Http\Controllers;

use App\Models\SensorReading;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;

class AIController extends Controller
{
    public function chat(Request $request)
    {
        $request->validate([
            'message' => 'required|string',
        ]);

        $userMessage = $request->input('message');

        // Fetch latest sensor data for context
        // $latestReading = SensorReading::latest()->first();
        $latestReading = null;

        $context = "You are an AI assistant for a hydroponic lettuce monitoring system. ";
        $context .= "IMPORTANT: Respond in English. Keep technical terms in English (e.g., 'pH Level', 'TDS', 'Pump').\n";

        if ($latestReading) {
            $context .= "Here is the current system status:\n";
            $context .= "- Temperature: {$latestReading->temperature}°C\n";
            $context .= "- Humidity: {$latestReading->humidity}%\n";
            $context .= "- pH Level: {$latestReading->ph}\n";
            $context .= "- TDS (Nutrients): {$latestReading->tds} ppm\n";
            $context .= "- Water Pump: " . ($latestReading->pump_status ? 'ON' : 'OFF') . "\n";
            $context .= "- Ventilation Fan: " . ($latestReading->fan_status ? 'ON' : 'OFF') . "\n";
        } else {
            $context .= "The system is currently offline or has no sensor data available.\n";
        }

        $context .= "\nAnswer the user's question based on this data if relevant. Keep answers concise, helpful, and friendly.\n\n";
        $context .= "User Question: " . $userMessage;

        Log::info('AI Chat Request', ['message' => $userMessage]);

        $apiKey = config('services.gemini.key');
        if (!$apiKey) {
            Log::error('Gemini API Key is missing');
            return response()->json(['error' => 'AI Service configuration error.'], 500);
        }

        $url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={$apiKey}";

        try {
            // Log the request for debugging (remove in production if sensitive)
            Log::info('Sending request to Gemini API', ['url' => $url]);

            $response = Http::timeout(15)->withHeaders([
                'Content-Type' => 'application/json',
            ])->post($url, [
                'contents' => [
                    [
                        'parts' => [
                            ['text' => $context]
                        ]
                    ]
                ]
            ]);

            if ($response->successful()) {
                $data = $response->json();
                $aiResponse = $data['candidates'][0]['content']['parts'][0]['text'] ?? "I'm sorry, I couldn't generate a response.";

                return response()->json([
                    'response' => $aiResponse
                ]);
            } else {
                Log::error('Gemini API Error: ' . $response->body());
                return response()->json([
                    'error' => 'Failed to communicate with AI service.',
                    'details' => $response->body()
                ], 500);
            }
        } catch (\Exception $e) {
            Log::error('AI Controller Exception: ' . $e->getMessage());
            return response()->json([
                'error' => 'An internal error occurred.',
                'details' => $e->getMessage()
            ], 500);
        }
    }
}
