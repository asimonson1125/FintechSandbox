import matplotlib.pyplot as plt

def candle_plot(data, ax=None, width=0.8, colorup='green', colordown='red'):
  """
  Plots a candle chart from the given data.

  Args:
    data: A pandas DataFrame with the columns `open`, `high`, `low`, and `close`.
    ax: The matplotlib axes to plot the chart on. If None, a new figure and axes will be created.
    width: The width of the candles in units of the x-axis.
    colorup: The color of the candles for up days.
    colordown: The color of the candles for down days.

  Returns:
    The matplotlib axes that the chart was plotted on.
  """

  if ax is None:
    fig, ax = plt.subplots()

  for i in range(len(data)):
    open = data[i]['open']
    high = data[i]['high']
    low = data[i]['low']
    close = data[i]['close']
    ax.plot([i, i], [low, high], color='black', lw=1)
    ax.fill_between([i, i], [open, high], [close, low], color=colorup if close > open else colordown, alpha=0.5)

  ax.set_xticks(range(len(data)))
  ticks = []
  for i in range(0, len(data)): 
    if i % 60 == 0:
        ticks.append(data[i]['datetime'])
    else:
      ticks.append('')
  ax.set_xticklabels(ticks)
  ax.set_ylabel('Price')
  ax.set_title('Candlestick Chart')

  return ax
