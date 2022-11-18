
.PHONY: download_house_prices
download_house_prices:
	kaggle competitions download -c house-prices-advanced-regression-techniques
	mkdir -p data/house-prices
	unzip house-prices-advanced-regression-techniques.zip -d data/house-prices
	rm house-prices-advanced-regression-techniques.zip