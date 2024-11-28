import spidev
import time

# Setup SPI
spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 1350000  # kecepatan komunikasi SPI

def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    
    # Mengatur nilai ke 0 jika tidak valid (contoh ambang batas)
    if data > 1023:  # Ganti 1000 dengan ambang batas sesuai
        return 0
    return data

def convert_volts(data, v_ref=5.5):
    return (data * v_ref) / float(1023)

# Function to convert ADC data to pressure in bar
def convert_to_pressure(voltage):
    max_voltage = 4.5
    max_pressure = 12.0
    return (voltage / max_voltage) * max_pressure

# Data reading loop
try:
    while True:
        raw_value = read_channel(1)  # Ganti dengan channel yang sesuai (0-3)
        voltage = convert_volts(raw_value)
        pressure = convert_to_pressure(voltage)
    
        # Display reading result
        print("Voltage: {:.2f} V".format(voltage))
        print("ADC Value: {}".format(raw_value))
        print("Raw Pressure: {:.2f} bar".format(pressure))
    
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("Program dihentikan")
finally:
    spi.close()
