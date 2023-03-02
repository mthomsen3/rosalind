def dominant_probability(k, m, n):
    total = k + m + n
    dominant = (k / total) * ((k - 1) / (total - 1))
    dominant += (k / total) * (m / (total - 1))
    dominant += (k / total) * (n / (total - 1))
    dominant += (m / total) * (k / (total - 1))
    dominant += 0.75 * (m / total) * ((m - 1) / (total - 1))
    dominant += 0.5 * (m / total) * (n / (total - 1))
    dominant += (n / total) * (k / (total - 1))
    dominant += 0.5 * (n / total) * (m / (total - 1))
    return dominant

k = 16
m = 19
n = 29
print(dominant_probability(k, m, n))