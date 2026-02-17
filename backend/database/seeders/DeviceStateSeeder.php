<?php

namespace Database\Seeders;

use App\Models\DeviceState;
use Illuminate\Database\Seeder;

class DeviceStateSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        DeviceState::firstOrCreate(
            ['device' => 'pump'],
            ['is_on' => false]
        );

        DeviceState::firstOrCreate(
            ['device' => 'fan'],
            ['is_on' => false]
        );
    }
}
