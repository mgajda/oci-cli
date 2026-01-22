# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


"""The main purpose of this page is to have all the error messages which is being used in the Interactive CLI,
so updating those in the future should be easy, it is recommended not to call error messages from
outside this page, instead call get_error_message function"""

error_messages = {
    "invalid_input": "Invalid input. Please use TAB for suggestions, SPACE to select, ENTER to execute.\nFor help: Ctrl-H",
    "missing_required_params": "Missing required parameters (marked with *).\nUse TAB to see required parameters or type --help for documentation",
    "resource_search_failed": ("Resource search failed.\n"
                               "Possible causes:\n"
                               "  1. Missing IAM policy: Allow group <group> to read <resource> in compartment <compartment>\n"
                               "  2. Wrong compartment selected\n"
                               "  3. Resource doesn't exist\n"
                               "To check policies: oci iam policy list --compartment-id <tenancy-ocid>"),
    "no_items_found": ("No items found.\n"
                      "Try:\n"
                      "  1. Check compartment selection (use --compartment-id)\n"
                      "  2. Verify filters (remove or adjust --display-name, --lifecycle-state)\n"
                      "  3. Check region (use --region)\n"
                      "  4. Ensure resource exists: oci <service> <resource> list --all"),
    "try_again": ("Operation failed.\n"
                 "Troubleshooting:\n"
                 "  1. Check network connectivity\n"
                 "  2. Verify credentials: oci iam user get --user-id <your-user-ocid>\n"
                 "  3. Review the last command for syntax errors\n"
                 "  4. Enable debug mode: export OCI_CLI_DEBUG=1"),
    "history_clear": "History cleared successfully. Previous commands removed from interactive session.",
    "terminal_too_small": ("Terminal too small for interactive mode.\n"
                          "Minimum size: 80 columns x 24 rows\n"
                          "Current size can be checked with: tput cols && tput lines\n"
                          "Resize your terminal window and try again.")
}


def get_error_message(error, extra_text=""):
    if error in error_messages:
        error_message = error_messages[error]
        if extra_text:
            error_message += " " + extra_text
        return error_message
