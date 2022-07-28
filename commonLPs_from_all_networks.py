import pandas as pd

v2_mainnet = pd.read_csv("data/wallets/v2_mainnet.csv")
v3_mainnet = pd.read_csv("data/wallets/v2_mainnet.csv")
v3_op = pd.read_csv("data/wallets/v3_op.csv")
v3_polygon = pd.read_csv("data/wallets/v3_polygon.csv")

output = v2_mainnet.merge(v3_mainnet, on="wallet_addr", how="inner")
output = output.merge(v3_op, on="wallet_addr", how="inner")
output = output.merge(v3_polygon, on="wallet_addr", how="inner")
output.to_csv("commonLPs_from_all_networks.csv")