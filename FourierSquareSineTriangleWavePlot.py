import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
frequency = 50    # Frequency of the square wave in Hz
sample_rate = 1000  # Sample rate in Hz
duration = 1     # Duration in seconds

# Time array, Creates an array of time values over the specified duration
t_sq = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Square wave generation, Uses the sign of a sine wave to create a square wave.
square_wave = np.sign(np.sin(2 * np.pi * frequency * t_sq))

# Compute the Fourier Transform
fft_square_wave = np.fft.fft(square_wave)
# Calculate the frequencies corresponding to the FFT coefficients
frequencies_square_wave = np.fft.fftfreq(len(square_wave), 0.01)

# Plot the original square wave signal
plt.subplot(2, 1, 1)
plt.plot(t_sq, square_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Square Wave Signal')

# Plot the magnitude spectrum of the Square Wave Fourier Transform
plt.subplot(2, 1, 2)
plt.plot(frequencies_square_wave, np.abs(fft_square_wave))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Fourier Transform')
plt.tight_layout()
plt.show()



# Generate a sine signal
frequency_sinewave = 5    # Frequency in Hz
sample_rate = 100  # Sample rate in Hz
duration = 1     # Duration in seconds
t_sine = np.arange(0, 1, 1/sample_rate)    #
sine_wave = np.sin(2 * np.pi * frequency_sinewave * t_sine)   # + 0.5 * np.sin(2 * np.pi * 10 * t)

# Compute the Fourier Transform
fft_sinewave = np.fft.fft(sine_wave)

# Calculate the frequencies corresponding to the FFT coefficients
frequencies_sine_wave = np.fft.fftfreq(len(sine_wave), 0.01)

# Plot the sine wave signal
plt.subplot(2, 1, 1)
plt.plot(t_sine, sine_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original Signal')

# Plot the magnitude spectrum of the Sine Wave Fourier Transform
plt.subplot(2, 1, 2)
plt.plot(frequencies_sine_wave, np.abs(fft_sinewave))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Fourier Transform')
plt.tight_layout()
plt.show()

t_tri = np.linspace(0, 1, 500)  # Time vector
triangle_wave = signal.sawtooth(2 * np.pi * 5 * t_tri, width=0.5) 

# Compute the Fourier Transform
fft_triangle_wave = np.fft.fft(triangle_wave)

# Calculate the frequencies corresponding to the FFT coefficients
frequencies_triangle_wave = np.fft.fftfreq(len(triangle_wave), 0.01)
"""
plt.plot(t, triangle_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Triangle Wave')
plt.show()"""

# Plot the Triangle wave signal
plt.subplot(2, 1, 1)
plt.plot(t_tri, triangle_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Triangle Signal')

# Plot the magnitude spectrum of the Triangle Wave Fourier Transform
plt.subplot(2, 1, 2)
plt.plot(frequencies_triangle_wave, np.abs(fft_triangle_wave))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Fourier Transform')
plt.tight_layout()
plt.show()

#PLOT 4 MULTIPLE WAVES

# Plot the Sine wave signal
plt.subplot(4, 1, 1)
plt.plot(t_sine, sine_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sine Wave Signal')

# Plot the magnitude spectrum of the Sine Wave Fourier Transform
plt.subplot(4, 1, 2)
plt.plot(frequencies_sine_wave, np.abs(fft_sinewave))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Fourier Transform')


# Plot the Sqaure wave signal
plt.subplot(4, 1, 3)
plt.plot(t_sq, square_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Triangle Signal')

# Plot the magnitude spectrum of the Sine Wave Fourier Transform
plt.subplot(4, 1, 4)
plt.plot(frequencies_square_wave, np.abs(fft_square_wave))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Fourier Transform')

plt.tight_layout()
plt.show()