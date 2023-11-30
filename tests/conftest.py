import time

import pytest
from playwright.sync_api import Browser

from utils.file_utils.PathUtils import PathUtils


@pytest.fixture
def base_fixture(browser: Browser, request):
    yield browser

    if request.node.rep_call.outcome == "failed":
        for context in browser.contexts:
            for page in context.pages:
                page.screenshot(type="jpeg",
                                full_page=True,
                                path="{}/report/screenshots/screenshot{}.jpeg".format(PathUtils.get_root_project_dir(), time.time()))
