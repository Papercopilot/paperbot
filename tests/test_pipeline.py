import paperbot
import argparse

def set_arguments():
    parser.add_argument('--confs', nargs='+', help='conference names', default=['iclr', 'nips', 'icml', 'corl', 'emnlp'])
    parser.add_argument('--years', nargs='+', help='years', default=range(2024, 2012, -1))
    
    # 
    parser.add_argument('--openreview', action='store_true', help='parse from openreview')
    parser.add_argument('--site', action='store_true', help='parse from site')
    
    # setup directories
    parser.add_argument('--root_dir', type=str, help='root directory for logs', default='../logs')
    parser.add_argument('--openreview_dir', type=str, help='directory for openreview logs', default='openreview')
    parser.add_argument('--paperlists_dir', type=str, help='directory for site logs', default='paperlists')
    parser.add_argument('--statistics_dir', type=str, help='directory for summary logs', default='stats')
    
    # 
    parser.add_argument('--parse_keywords', action='store_true', help='extract keywords', default=True)

def test_pipeline(args):
    p = paperbot.Pipeline(args)
    assert p is not None
    p.launch()
    p.save_summary()
    p.save_keywords()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    set_arguments()
    args = parser.parse_args()
    args.confs = ['iclr']
    args.years = [2023]
    
    test_pipeline(args)