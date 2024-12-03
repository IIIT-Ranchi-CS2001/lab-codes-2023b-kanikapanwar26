import matplotlib.pyplot as plt

# Data for Madhya Pradesh
mp_parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]
mp_total_seats = sum(mp_seats)
mp_percentages = [(seats / mp_total_seats) * 100 for seats in mp_seats]

# Data for Rajasthan
raj_parties = ['INC', 'BJP', 'BSP', 'Others']
raj_seats = [69, 115, 2, 13]
raj_total_seats = sum(raj_seats)
raj_percentages = [(seats / raj_total_seats) * 100 for seats in raj_seats]

# Colors for the pie charts
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create subplots for pie charts
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Explode largest percentage
explode_mp = [0.1 if p == max(mp_percentages) else 0 for p in mp_percentages]
explode_raj = [0.1 if p == max(raj_percentages) else 0 for p in raj_percentages]

# Madhya Pradesh pie chart
axs[0].pie(mp_percentages, labels=[f'{party} ({p:.1f}%)' for party, p in zip(mp_parties, mp_percentages)],
           explode=explode_mp, autopct='%1.1f%%', colors=colors, startangle=90)
axs[0].set_title('Madhya Pradesh Assembly Elections 2023')

# Rajasthan pie chart
axs[1].pie(raj_percentages, labels=[f'{party} ({p:.1f}%)' for party, p in zip(raj_parties, raj_percentages)],
           explode=explode_raj, autopct='%1.1f%%', colors=colors, startangle=90)
axs[1].set_title('Rajasthan Assembly Elections 2023')

# Adjust layout
plt.tight_layout()

fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
x = range(len(mp_parties))  # Common x-axis positions
bar_width = 0.35

# Bar chart for Madhya Pradesh and Rajasthan
ax_bar.bar([pos - bar_width / 2 for pos in x], mp_seats, bar_width, label='Madhya Pradesh', color='#1f77b4')
ax_bar.bar([pos + bar_width / 2 for pos in x], raj_seats, bar_width, label='Rajasthan', color='#ff7f0e')

# Adding labels, title, and legend
ax_bar.set_xticks(x)
ax_bar.set_xticklabels(mp_parties)
ax_bar.set_xlabel('Parties')
ax_bar.set_ylabel('Seats Won')
ax_bar.set_title('Seat Shares in Assembly Elections 2023')
ax_bar.legend()

# Show all plots
plt.show()