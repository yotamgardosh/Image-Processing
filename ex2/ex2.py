import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import soundfile as sf


def plot_fourier_transform(audio_data, sample_rate, title, directory):

    # Calculate the Fourier Transform with centered frequencies
    frequencies = np.fft.fftfreq(len(audio_data), d=1 / sample_rate)
    fft_values = np.fft.fft(audio_data)

    # Shift the zero frequency component to the center
    fft_values = np.fft.fftshift(fft_values)
    frequencies = np.fft.fftshift(frequencies)

    # Plot the Fourier Transform
    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, np.abs(fft_values))
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.xlim(-sample_rate / 2, sample_rate / 2)  # Display frequencies from -Nyquist to Nyquist
    plt.savefig(directory + title + '.png')
    plt.show()


def plot_specgram(audio_data, sample_rate, title, directory, window_size=1024, hop_length=512):
    _, _, Sxx, im = plt.specgram(audio_data, NFFT=window_size, Fs=sample_rate, noverlap=hop_length, cmap='plasma')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title(title)
    plt.colorbar(im, label='Magnitude (dB)')
    plt.savefig(directory + title + '.png')
    plt.show()


def clean_q1(audio_data) -> np.array:
    """
    Denoises the q1 audio data.

    Parameters:
    - audio_data: numpy array, audio data

    Returns:
    - modified_data: denoised version of the q1 audio data
    """
    # Compute the Fourier Transform of the audio data
    fft_result = np.fft.fft(audio_data)

    # Find the index of the highest magnitude frequency in the Fourier Transform
    index_max_magnitude = np.argmax(np.abs(fft_result))

    # Set the magnitudes of max frequency to zero
    fft_result[index_max_magnitude] = 0

    # Shift the index to the corresponding negative frequency
    index_min_magnitude = len(fft_result) - index_max_magnitude

    # Set the magnitudes of the corresponding negative frequency to zero
    fft_result[index_min_magnitude] = 0

    # Perform Inverse Fourier Transform (IFFT) to obtain the denoised audio data
    modified_data = np.fft.ifft(fft_result).real

    return modified_data


def clean_q2(audio_data, frequencies):
    """
    Denoises the q2 audio data.

    Parameters:
    - audio_data: numpy array, audio data
    - sample_rate: int, sample rate of the audio data
    - frequencies: numpy array, frequencies corresponding to the Fourier Transform

    Returns:
    - modified_data: denoised version of the q2 audio data
    """
    # Compute the Fourier Transform of the audio data
    fft_result = np.fft.fft(audio_data)

    # Define the frequency range to be set to zero (adjust as needed)
    frequency_range = (580, 650)

    # Identify the indices corresponding to the frequencies within the specified range
    indices_to_zero = np.where((frequencies >= frequency_range[0]) & (frequencies <= frequency_range[1]))[0]

    fft_result[indices_to_zero] = 0

    frequency_range = (-650, -580)

    # Identify the indices corresponding to the frequencies within the specified range
    indices_to_zero = np.where((frequencies >= frequency_range[0]) & (frequencies <= frequency_range[1]))[0]

    # Set the magnitudes of the frequencies within the specified range to zero
    fft_result[indices_to_zero] = 0

    # Perform Inverse Fourier Transform (IFFT) to obtain the denoised audio data
    modified_data = np.fft.ifft(fft_result).real

    return modified_data


def q2():
    path_to_audio = 'q2.wav'
    path_to_dir = 'q2_graphs/'

    # Load the audio file
    sample_rate, audio_data = wavfile.read(path_to_audio)

    # Calculate the frequencies
    frequencies = np.fft.fftfreq(len(audio_data), d=1 / sample_rate)

    plot_fourier_transform(audio_data, sample_rate, 'q2 - Fourier Transform of Audio Wave', path_to_dir)

    # Plot the original spectrogram using the custom function
    plot_specgram(audio_data, sample_rate, 'q2 - Original Spectrogram', path_to_dir)

    # Clean the spectrogram
    cleaned_data = clean_q2(audio_data, frequencies)

    # Plot after cleaning
    plot_fourier_transform(cleaned_data, sample_rate, 'q2 - Fourier Transform of De-noised Audio Wave', path_to_dir)

    # Show cleaned spectrogram
    plot_specgram(cleaned_data, sample_rate, 'q2 - De-noised Spectrogram', path_to_dir)

    # sf.write("cleaned_q2.wav", cleaned_data, sample_rate)


def q1():
    path_to_audio = 'q1.wav'
    path_to_dir = 'q1_graphs/'

    # Load the audio file
    sample_rate, audio_data = wavfile.read(path_to_audio)

    plot_fourier_transform(audio_data, sample_rate, 'q1 - Fourier Transform of Audio Wave', path_to_dir)

    # Plot the original spectrogram using the custom function
    plot_specgram(audio_data, sample_rate, 'q1 - Original Spectrogram', path_to_dir)

    # Clean the spectrogram
    cleaned_data = clean_q1(audio_data)

    # Plot after cleaning
    plot_fourier_transform(cleaned_data, sample_rate, 'q1 - Fourier Transform of De-noised Audio Wave', path_to_dir)

    # Show cleaned spectrogram
    plot_specgram(cleaned_data, sample_rate, 'q1 - De-noised Spectrogram', path_to_dir)

    # sf.write("C:University/CS/Image_Processing/ex2/cleaned_q1.wav",'w' ,cleaned_data, sample_rate)


if __name__ == "__main__":
    q1()
    q2()
