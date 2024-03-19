# import random 

# slot_symbols = ["🍒", "🍊", "🍋", "🍇", "🍓", "💰"]

# prize_map = {
#     "🍒": 2,
#     "🍊": 4,
#     "🍋": 6,
#     "🍇": 8,
#     "🍓": 10,
#     "💰": 50
# }
# probabilities = [
#     0.4,
#     0.25,
#     0.15,
#     0.1,
#     0.05,
#     0.05
# ]


# total_value = 0
# value = 0
# for i in range(1_000_000):
#     picks = random.choices(slot_symbols, weights=probabilities, k=3)
#     for thing in picks:
#         value += prize_map[thing]

#     if picks[0] == picks[1] and picks[1] == picks[2]:
#         value = value * 2
    
#     total_value += value
#     value = 0
# total_value = total_value / 1_000_000
# print(total_value)
#slot machine test