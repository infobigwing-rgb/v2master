import unittest
from unittest.mock import MagicMock, patch

from core.device_detector import DeviceDetector
from core.logger import Logger


class DeviceDetectorTests(unittest.TestCase):
    @patch('core.device_detector.USBScanner')
    def test_match_android_device_by_vid_pid(self, mock_scanner):
        scanner = mock_scanner.return_value
        scanner.list_devices.return_value = []
        detector = DeviceDetector(logger=Logger())
        usb_device = MagicMock()
        usb_device.vendor_id = int('18d1', 16)
        usb_device.product_id = int('4ee2', 16)
        usb_device.serial_number = 'ABC123'
        usb_device.product = 'Pixel'
        usb_device.manufacturer = 'Google'
        with patch.object(detector, '_load_device_database', return_value={'android': {'vendors': [{'vid': '0x18d1', 'pid': '0x4ee2', 'mode': 'adb', 'brand': 'Google'}]}}):
            detector.database = detector._load_device_database()
            match = detector._match_android_device(usb_device)
        self.assertIsNotNone(match)
        self.assertEqual(match['platform'], 'android')
        self.assertEqual(match['mode'], 'adb')

    @patch('core.device_detector.USBScanner')
    def test_match_ios_device_by_mode(self, mock_scanner):
        scanner = mock_scanner.return_value
        scanner.list_devices.return_value = []
        detector = DeviceDetector(logger=Logger())
        usb_device = MagicMock()
        usb_device.vendor_id = int('05ac', 16)
        usb_device.product_id = int('1290', 16)
        usb_device.serial_number = 'IOS123'
        usb_device.product = 'iPhone'
        usb_device.manufacturer = 'Apple'
        with patch.object(detector, '_load_device_database', return_value={'ios': {'vendor_id': '0x05ac', 'normal': ['1290'], 'recovery': [], 'dfu': []}}):
            detector.database = detector._load_device_database()
            match = detector._match_ios_device(usb_device)
        self.assertIsNotNone(match)
        self.assertEqual(match['platform'], 'ios')
        self.assertEqual(match['mode'], 'normal')


if __name__ == '__main__':
    unittest.main()
