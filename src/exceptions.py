class ForecastingError(Exception):
    """Base category for all forecasting errors"""
    pass

class DataNotFoundError(ForecastingError):
    """Raised when data files are missing"""
    pass

class ModelTrainingError(ForecastingError):
    """Raised when model training fails"""
    pass

class PreprocessingError(ForecastingError):
    """Raised when preprocessing steps fail"""
    pass
