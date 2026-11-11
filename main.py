from pathlib import Path
import os


def main() -> None:
    summary_path = Path(__file__).with_name("summary.txt")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(summary_path.read_bytes())


if __name__ == "__main__":
    main()
