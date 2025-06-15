from config import num_of_steps, data_filepath, report_filepath, analytics_filepath
from analytics import Research
import logging

def make_report():
    research = Research(data_filepath)
    list_of_coins = research.file_reader()

    tails, heads = research.Calculation(list_of_coins).counts()
    head_fraction, tail_fraction = research.Calculation(list_of_coins).Fractions()

    analytics = Research.Analytics(list_of_coins)
    random_predict = analytics.predict_random(num_of_steps)
    last_predict = analytics.predict_last()

    report = (
        "Report\n"
        f"We have made {len(list_of_coins)} observations from tossing a coin:\n"
        f"{tails} tails and {heads} heads\n"
        f"Tails: {tail_fraction:.1f}%\n"
        f"Heads: {head_fraction:.1f}%\n\n"
        "Random predictions:\n"
        + "\n".join(str(prediction) for prediction in random_predict) + "\n\n"
        f"Last observation:\n{last_predict}\n"
    )

    analytics.save_file(report, report_filepath.split('.')[0], report_filepath.split('.')[1])

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=analytics_filepath,
        filemode="w"
    )
    research_result = Research(data_filepath)
    try:
        make_report()
        research_result.send_tg_message("Report generated successfully")
        logging.info("Report generated successfully")
    except Exception as e:
        research_result.send_tg_message("Error generating report")
        logging.error("Error generating report")


