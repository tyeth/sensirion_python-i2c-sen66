#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2024 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 1.0.1
# Product:       sen66
# Model-Version: 1.2.0
#

import pytest
from sensirion_i2c_sen66.device import Sen66Device


@pytest.fixture
def sensor(channel_provider):
    channel_provider.i2c_frequency = 100e3
    channel_provider.supply_voltage = 3.3
    with channel_provider:
        channel = channel_provider.get_channel(slave_address=0x6B,
                                               crc_parameters=(8, 0x31, 0xff, 0x0))
        yield Sen66Device(channel)


def test_perform_forced_co2_recalibration1(sensor):
    correction = sensor.perform_forced_co2_recalibration(600)
    print(f"correction: {correction}; "
          )


def test_get_product_name1(sensor):
    product_name = sensor.get_product_name()
    print(f"product_name: {product_name}; "
          )


def test_get_serial_number1(sensor):
    serial_number = sensor.get_serial_number()
    print(f"serial_number: {serial_number}; "
          )


def test_get_version1(sensor):
    (firmware_major, firmware_minor, firmware_debug, hardware_major, hardware_minor, protocol_major, protocol_minor,
     padding
     ) = sensor.get_version()
    print(f"firmware_major: {firmware_major}; "
          f"firmware_minor: {firmware_minor}; "
          f"firmware_debug: {firmware_debug}; "
          f"hardware_major: {hardware_major}; "
          f"hardware_minor: {hardware_minor}; "
          f"protocol_major: {protocol_major}; "
          f"protocol_minor: {protocol_minor}; "
          f"padding: {padding}; "
          )


def test_device_reset1(sensor):
    sensor.device_reset()


def test_start_continuous_measurement1(sensor):
    sensor.start_continuous_measurement()
    (mass_concentration_pm1p0, mass_concentration_pm2p5, mass_concentration_pm4p0, mass_concentration_pm10p0, humidity,
     temperature, voc_index, nox_index, co2
     ) = sensor.read_measured_values()
    print(f"mass_concentration_pm1p0: {mass_concentration_pm1p0}; "
          f"mass_concentration_pm2p5: {mass_concentration_pm2p5}; "
          f"mass_concentration_pm4p0: {mass_concentration_pm4p0}; "
          f"mass_concentration_pm10p0: {mass_concentration_pm10p0}; "
          f"humidity: {humidity}; "
          f"temperature: {temperature}; "
          f"voc_index: {voc_index}; "
          f"nox_index: {nox_index}; "
          f"co2: {co2}; "
          )
    (mass_concentration_pm1p0, mass_concentration_pm2p5, mass_concentration_pm4p0, mass_concentration_pm10p0,
     ambient_humidity, ambient_temperature, voc_index, nox_index, co2
     ) = sensor.read_measured_values_as_integers()
    print(f"mass_concentration_pm1p0: {mass_concentration_pm1p0}; "
          f"mass_concentration_pm2p5: {mass_concentration_pm2p5}; "
          f"mass_concentration_pm4p0: {mass_concentration_pm4p0}; "
          f"mass_concentration_pm10p0: {mass_concentration_pm10p0}; "
          f"ambient_humidity: {ambient_humidity}; "
          f"ambient_temperature: {ambient_temperature}; "
          f"voc_index: {voc_index}; "
          f"nox_index: {nox_index}; "
          f"co2: {co2}; "
          )
    (padding, data_ready
     ) = sensor.get_data_ready()
    print(f"padding: {padding}; "
          f"data_ready: {data_ready}; "
          )
    sensor.stop_measurement()

