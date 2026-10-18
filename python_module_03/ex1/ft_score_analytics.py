import sys


def score_check(name: str) -> int:
    try:
        temp = int(name)
        return temp
    except ValueError:
        raise ValueError(f"Invalid parameter: '{name}'")


def test_scores() -> None:
    scores = sys.argv
    valid_scores = []
    
    if len(scores) == 1:
        print("No scores provided. Usage: ", end="")
        print("python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        for name in scores[1:]:
            try:
                valid_scores.append(score_check(name))
            except ValueError as e:
                print(e)
    print_scores(valid_scores)


def print_scores(scores: list) -> None:
    if not scores:
        print("No scores provided. Usage: ", end="")
        print("python3 ft_score_analytics.py <score1> <score2> ...")
        return
        
    print(f"Total score: {sum(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")

if __name__ == "__main__":
    test_scores()
