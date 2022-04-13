"""Submission for the Making the Grade exercise.
Exercise description is found at:
https://exercism.org/tracks/python/exercises/making-the-grade
"""
from typing import Union


def round_scores(student_scores: list[Union[float, int]]) -> list[int]:
    """Round all provided student scores.

    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    return [round(score) for score in student_scores]

    # With function application
    # return map(round, student_scores)

    # With loop:
    # results = []
    # for student_score in student_scores:
    #     results.append(round(student_score))
    # return results


def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    return sum([1 for score in student_scores if score <= 40])

    # With filter:
    # return len(list(filter(lambda score: score <= 40, student_scores)))

    # # With loop:
    # count = 0
    # for student_score in student_scores:
    #     if student_score <= 40:
    #         count += 1
    # return count


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    return [score for score in student_scores if score >= threshold]

    # With filter:
    # return list(filter(lambda score: score >= threshold, student_scores))

    # With loop:
    # results = []
    # for student_score in student_scores:
    #     if student_score >= threshold:
    #         results.append(student_score)
    # return results


def letter_grades(highest: int) -> list[int]:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    increment = (highest - 40) // 4
    # With simple range:
    return list(range(41, highest, increment))

    # With loop:
    # grades_thresholds = []
    # for level in range(41, highest, increment):
    #     grades_thresholds.append(level)
    # return grades_thresholds


def student_ranking(
    student_scores: list[int], student_names: list[str]
) -> list[str]:
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """
    # With list comprehension:
    return [
        f"{rank}. {student_name}: {score}"
        for rank, student_name, score in zip(
            range(1, len(student_names) + 1), student_names, student_scores
        )
    ]

    # With loop:
    # results = []
    # for index, student_info in enumerate(zip(student_names, student_scores)):
    #     rank = index + 1
    #     student_name, score = student_info
    #     results.append(f"{rank}. {student_name}: {score}")
    # return results


def perfect_score(
    student_info: list[list[Union[str, int]]]
) -> list[Union[str, int]]:
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    # With loop:
    for student in student_info:
        _, score = student
        if score == 100:
            return student
    return []

    # With generators:
    # return next(
    #     (
    #         [student_name, 100]
    #         for student_name, student_score in student_info
    #         if student_score == 100
    #     ),
    #     [],
    # )
