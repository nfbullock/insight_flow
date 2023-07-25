import os

import pytz

import config
import utilities


def _extract_microjournal(filename: str):
    if filename.startswith(utilities.TODAY):
        # TODO: (i)nclude, (u)pdate, (a)ppend, (d)elete
        with open(file_path) as f:
            return f.read()


def _get_modified_files():
    start_of_day_local = utilities.get_start_of_day_datetime()
    files_modified, micro_journals = [], []
    for dirpath, dirnames, filenames in os.walk(config.notes_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if any(i in file_path for i in config.notes_ignored_directories):
                continue
            elif config.notes_micro_journal_subdirectory in dirpath:
                with open(file_path) as f:
                    entry = f.read()
                micro_journals.append(entry)
            else:
                file_modified_time_local = (
                    utilities.get_file_modified_datetime(file_path)
                )
                if file_modified_time_local > start_of_day_local:
                    file_path = file_path.replace(config.notes_directory, "")
                    file_path = file_path.replace(".md", "").strip("/")
                    readable_title = "-".join(file_path.split("/"))
                    files_modified.append(readable_title)
    return {"files_modified": files_modified, "micro_journals": micro_journals}


def _write_microjournal(text):
    now = utilities.NOW_LOCAL.strftime(config.unique_date_str)
    filename = f"{now}.md"
    with open(f"{config.notes_micro_journal_path}/{filename}", "w") as f:
        f.write(text)


def quick_add():
    text = input("input: ")
    _write_microjournal(text)


def review():
    utilities.nag_prompt(
        "Obsidian review, make sure and open your phone to ensure a sync happens"
    )
    return _get_modified_files()


if __name__ == "__main__":
    print(_get_modified_files())
