<?php

namespace App\Http\Controllers;

use App\Models\DeviceState;
use Illuminate\Http\Request;

class DeviceStateController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return response()->json(DeviceState::all());
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        // Not typically used for toggle, but can be for initial setup
        $validated = $request->validate([
            'device' => 'required|string|unique:device_states',
            'is_on' => 'boolean',
        ]);
        
        $device = DeviceState::create($validated);
        return response()->json($device, 201);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $device)
    {
        $validated = $request->validate([
            'is_on' => 'required|boolean',
        ]);

        $state = DeviceState::updateOrCreate(
            ['device' => $device],
            ['is_on' => $validated['is_on']]
        );

        return response()->json($state);
    }

    /**
     * Toggle the device state.
     */
    public function toggle(string $device)
    {
        $state = DeviceState::firstOrCreate(
            ['device' => $device],
            ['is_on' => false]
        );

        $state->is_on = !$state->is_on;
        $state->save();

        return response()->json($state);
    }
}
