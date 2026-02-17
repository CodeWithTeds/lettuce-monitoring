<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SensorReading extends Model
{
    use HasFactory;

    protected $fillable = [
        'temperature',
        'humidity',
        'ph',
        'tds',
        'pump_status',
        'fan_status',
    ];

    protected $casts = [
        'temperature' => 'float',
        'humidity' => 'float',
        'ph' => 'float',
        'tds' => 'float',
        'pump_status' => 'boolean',
        'fan_status' => 'boolean',
    ];
}
