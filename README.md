# House Price Prediction

## Repository Overview

This repository contains the code and resources for the  house price prediction. The objective is to develop an AI model that can accurately predict the value of real estate properties based on various influential factors.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Shengwei0516/House-Price-Prediction.git
    ```
2. Navigate to the project directory:
    ```bash
    cd House-Price-Prediction
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Data Preparation

1. Place your training data in the `data` directory. Ensure your data is in a suitable format (e.g., CSV).
2. Preprocess the data using the provided scripts in the `preprocessing` directory. This may include steps such as cleaning, normalization, and feature extraction.


### Adding External Information

Use the `external_data.py` script to incorporate additional external information into your dataset:

```bash
python external_data.py
```

### Model Training and Testing

Use the `main.py` script to load the data, train the model, and test it:

```bash
python main.py
```

## Project Structure

- `LICENSE`: The license for the project.
- `README.md`: The readme file you are currently reading.
- `external_data.py`: Script for fetching and processing external data.
- `main.py`: Main script to run the project.
- `requirements.txt`: List of required Python packages.
- `data/`: Directory for storing datasets (not shown, but should be created).

## Contributing

We welcome contributions from the community. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

### Issues

If you encounter any issues or have suggestions for improvements, please feel free to open an issue in the GitHub repository.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or inquiries, please contact m11207330@mail.ntust.edu.tw

## Acknowledgements

We would like to express our gratitude to the following organizations for providing the data and organizing the YongFeng AI GO Competition:

### Organizer: SinoPac Holdings
Thank you to SinoPac Holdings for providing the valuable data and hosting this competition.

### Co-organizer: Trend Micro
Thank you to Trend Micro for their support and collaboration in making this competition possible.

Your efforts and contributions are greatly appreciated.
