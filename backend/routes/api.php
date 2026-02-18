<?php

use App\Http\Controllers\SensorController;
use App\Http\Controllers\DeviceStateController;
use App\Http\Controllers\AIController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get('/sensor-readings/latest', [SensorController::class, 'index']);
Route::post('/sensor-readings', [SensorController::class, 'store']);

Route::get('/device-states', [DeviceStateController::class, 'index']);
Route::post('/device-states/{device}/toggle', [DeviceStateController::class, 'toggle']);
Route::post('/device-states/{device}', [DeviceStateController::class, 'update']);

Route::post('/ai/chat', [AIController::class, 'chat']);
