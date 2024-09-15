"""
YTubeInsight: A Python package for YouTube channel analytics.

This package provides tools to analyze YouTube channels, including
video count tracking and detailed video information extraction.
"""

from .analyzer import analyze_channel
from .exceptions import YTubeInsightError

__all__ = ['analyze_channel', 'YTubeInsightError']
__version__ = '0.1.0'