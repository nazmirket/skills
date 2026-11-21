import base64
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


CHECKER = Path(__file__).resolve().parents[1] / "skills/design/scripts/full-page.mjs"
# A lossless 6 × 12 pixel RGB image.
PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAYAAAAMCAIAAADONVt5AAAACXBIWXMAAAPoAAAD6AG1"
    "e1JrAAAAD0lEQVQImWP4jwEYhpsQANZF1ynVY39PAAAAAElFTkSuQmCC"
)


@unittest.skipUnless(shutil.which("node"), "The optional PNG checker runs in Node")
class DesignCaptureTest(unittest.TestCase):
    def check_image(self, width, height, density, image=PNG):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "original.png"
            path.write_bytes(image)
            return subprocess.run(
                ["node", str(CHECKER), str(path), str(width), str(height), str(density)],
                text=True, capture_output=True,
            )

    def test_full_native_image_and_fractional_density_rounding(self):
        for geometry in ((3, 6, 2), (2, 4, 3), (3, 6, 2.1)):
            with self.subTest(geometry=geometry):
                result = self.check_image(*geometry)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("6×12", result.stdout)

    def test_rejects_viewport_crop_low_density_and_incomplete_file(self):
        for label, geometry, image in (
            ("viewport only", (3, 12, 2), PNG),
            ("clipped width", (4, 6, 2), PNG),
            ("density too low", (6, 12, 1), PNG),
            ("missing end", (3, 6, 2), PNG[:-12]),
        ):
            with self.subTest(label=label):
                self.assertNotEqual(self.check_image(*geometry, image=image).returncode, 0)

    def test_cli_runs_through_a_linked_skill_install(self):
        with tempfile.TemporaryDirectory() as temp:
            skill = Path(temp) / "design"
            skill.symlink_to(CHECKER.parents[1], target_is_directory=True)
            result = subprocess.run(["node", str(skill / "scripts" / CHECKER.name)], text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Usage", result.stderr)
