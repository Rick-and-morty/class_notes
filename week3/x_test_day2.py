def hand_counter(hand):
    total = 0
    for card in hand:
        if card in ["K", "Q", "J"]:
            total += 10
        elif card == "A":
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total


def test_hand_counter_counts_up_all_vals_in_a_list():
    hand = [2, 4, 6]
    result = hand_counter(hand)
    assert result == 12


def test_hand_counter_counts_up_all_vals_in_list_K():
    hand = ["K", 4]
    result = hand_counter(hand)
    assert result == 14


def test_hand_counter_counts_up_all_vals_in_list_Q():
    hand = ["Q", 10]
    result = hand_counter(hand)
    assert result == 20


def test_hand_counter_counts_up_all_vals_in_list_J():
    hand = ["J", 4]
    result = hand_counter(hand)
    assert result == 14


def test_hand_counter_counts_up_all_vals_in_list_A():
    hand = ["A", 4]
    result = hand_counter(hand)
    assert result == 15


def test_hand_counter_counts_up_all_vals_in_list_A_as_1():
    hand = ["A", "J", 10]
    result = hand_counter(hand)
    assert result == 21


def test_hand_counter_counts_up_all_vals_in_list_A_as_1_and_11():
    hand = ["A", 10, "J"]
    result = hand_counter(hand)
    assert result == 20
