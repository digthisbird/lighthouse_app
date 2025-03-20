import pytest
from unittest.mock import MagicMock, patch
import pygame

from project import (
    roll_extra_die,
    draw_extra_die,
    draw_extra_die_button,
    handle_extra_die_click,
)

#mock needed to emulate pygame for tests without initializing pygame
@pytest.fixture
def mock_screen():
    return MagicMock()

@pytest.fixture
def mock_font():
    return MagicMock()

def test_roll_extra_die():
    result = roll_extra_die()
    assert 1 <= result <= 6

def test_draw_extra_die(mock_screen):
    mock_images = [MagicMock() for _ in range(6)]
    draw_extra_die(mock_screen, mock_images, 0, 100, 100)
    mock_screen.blit.assert_called_once()

def test_handle_extra_die_click():
    mock_event_click = MagicMock(type=pygame.MOUSEBUTTONDOWN)
    mock_rect = pygame.Rect(50, 50, 100, 100)
    #click inside the rect
    pygame.mouse.get_pos = MagicMock(return_value=(75, 75))
    assert handle_extra_die_click(mock_event_click, mock_rect) is True
    #click outside the rect
    pygame.mouse.get_pos = MagicMock(return_value=(10, 10))
    assert handle_extra_die_click(mock_event_click, mock_rect) is False

@patch('pygame.draw.rect')
def test_draw_extra_die_button(mock_draw_rect,mock_screen, mock_font):
    mock_rect = MagicMock()
    mock_rect.center = (100,75)
  
    pygame.mouse.get_pos = MagicMock(return_value=(75,75))
    draw_extra_die_button(mock_screen, mock_rect, mock_font)
    
    mock_font.render.assert_called_once()
    mock_screen.blit.assert_called_once()





