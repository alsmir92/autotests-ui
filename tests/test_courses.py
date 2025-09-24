import pytest
from playwright.sync_api import Page, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    course_head = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(course_head).to_have_text("Courses")

    folder_element = page.get_by_test_id("courses-list-empty-view-icon")
    expect(folder_element).to_be_visible()

    title_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(title_text).to_have_text("There is no results")

    description_text = page.get_by_test_id(
        "courses-list-empty-view-description-text")
    expect(description_text).to_have_text(
        "Results from the load test pipeline will be displayed here")
