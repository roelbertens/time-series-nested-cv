import logging

import numpy as np
import pandas as pd


class CustomTimeSeriesSplit:

    def __init__(self,
                 train_set_size: int,
                 test_set_size: int
                 ):
        """
        :param train_set_size: data points (days) in each fold for the train set
        :param test_set_size: data points (days) in each fold for the test set
        """
        self.train_set_size = train_set_size
        self.test_set_size = test_set_size
        self._logger = logging.getLogger(__name__)

    def split(self,
              x: np.array,
              y: np.array = None) -> (np.array, np.array):
        """Return train/test split indices.

        :param x: time series to use for prediction, shape (n_samples, n_features)
        :param y: time series to predict, shape (n_samples, n_features)
        :return: (train_indices, test_indices)

        Note: index of both x and y should be of type datetime.
        """
        if y is not None:
            assert x.index.equals(y.index)
        split_points = self.get_split_points(x)
        for split_point in split_points:
            is_train = (x.index < split_point) & (x.index >= split_point -
                                                  pd.Timedelta(self.train_set_size, unit='D'))
            is_test = (x.index >= split_point) & (x.index < split_point +
                                                  pd.Timedelta(self.test_set_size, unit='D'))
            if not is_train.any() or not is_test.any():
                self._logger.warning('Found %d train and %d test observations '
                                     'skipping fold for split point %s',
                                     is_train.sum(), is_test.sum(), split_point)
                continue
            dummy_ix = pd.Series(range(0, len(x)), index=x.index)
            ix_train = dummy_ix.loc[is_train].values
            ix_test = dummy_ix.loc[is_test].values
            if ix_train is None or ix_test is None:
                self._logger.warning('Found no data for train or test period, '
                                     'skipping fold for split date %s',
                                     split_point)
                continue
            yield ix_train, ix_test

    def get_split_points(self, x: np.array) -> pd.DatetimeIndex:
        """Get all possible split point dates"""
        start = x.index.min() + pd.Timedelta(self.train_set_size, unit='D')
        end = x.index.max() - pd.Timedelta(self.test_set_size - 1, unit='D')
        self._logger.info(f'Generating split points from {start} to {end}')
        split_range = pd.date_range(start, end, freq='D')
        first_split_point =  (len(split_range) + self.test_set_size - 1) % self.test_set_size
        return split_range[first_split_point::self.test_set_size]
