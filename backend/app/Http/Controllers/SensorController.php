<?php

namespace App\Http\Controllers;

use App\Models\SensorReading;
use Illuminate\Http\Request;

class SensorController extends Controller
{
    /**
     * Display the latest sensor reading.
     */
    public function index()
    {
        return response()->json(SensorReading::latest()->first());
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $validated = $request->validate([
            'temperature' => 'nullable|numeric',
            'humidity' => 'nullable|numeric',
            'ph' => 'nullable|numeric',
            'tds' => 'nullable|numeric',
            'pump_status' => 'boolean',
            'fan_status' => 'boolean',
        ]);

        $reading = SensorReading::create($validated);

        return response()->json($reading, 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
