import logging
import time

import schedule

from run_pipeline import main as run_pipeline


is_running = False


def scheduled_job() -> None:
    """Run pipeline job with overlap protection."""
    global is_running

    if is_running:
        logging.warning("Previous pipeline run is still running. Skipping this run.")
        return

    try:
        is_running = True
        logging.info("Scheduled pipeline run started.")
        run_pipeline()
        logging.info("Scheduled pipeline run completed.")
    finally:
        is_running = False


def main() -> None:
    """Start scheduler."""
    logging.basicConfig(
        filename="logs/scheduler.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    schedule.every(30).seconds.do(scheduled_job)

    print("Scheduler started. Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()