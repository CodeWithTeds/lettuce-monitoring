<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class DeviceState extends Model
{
    use HasFactory;

    protected $fillable = [
        'device',
        'is_on',
    ];

    protected $casts = [
        'is_on' => 'boolean',
    ];
}
