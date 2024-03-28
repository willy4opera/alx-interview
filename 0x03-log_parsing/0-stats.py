#!/usr/bin/python3

'''Parsing HTTP request logs with python.
'''
import re


def input_extractor(input_line):
    '''Fetches sections of a line of an HTTP request logs.
    '''
    expt = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    details = {
        'status_code': 0,
        'file_size': 0,
    }
    log_pattern = '{}\\-{}{}{}{}\\s*'.format(expt[0], expt[1], expt[2], expt[3], expt[4])
    exp_match = re.fullmatch(log_pattern, input_line)
    if exp_match is not None:
        status_code = exp_match.group('status_code')
        file_size = int(exp_match.group('file_size'))
        details['status_code'] = status_code
        details['file_size'] = file_size
    return details


def print_stat(total_file_size, status_codes_stats):
    '''show the accumulated stats of the HTTP request log.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for stat_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(stat_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(stat_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = input_extractor(line)
    stat_code = line_info.get('status_code', '0')
    if stat_code in status_codes_stats.keys():
        status_codes_stats[stat_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_stat(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_stat(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
