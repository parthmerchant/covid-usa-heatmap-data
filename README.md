# Interactive USA Choropleth Map visualizing COVID-19 Impact

Data joins and filtering with Apache Spark, cleaning with OpenRefine and visualization with Plotly, Seaborn, Pandas and Colorbrewer

--------------------------------------------------------------------------------------------
## Usage

1. Clone repository
2. Use `jupyter notebook` or `python3 -m notebook` to run the Jupyter Notebook. (You can view the Jupyter Notebook on GitHub, but Plotly Choropleth is interactive and requires you to run it in Jupyter Notebook.
3. Install dependencies using the command `pip3 install -r requirements.txt`. This will install Matplotlib, Pandas, Seaborn and Plotly. 
4. To run Spark Jobs, clone repository and upload directory to High Performance Cluster. Run `run_spark.sh`. 

--------------------------------------------------------------------------------------------

Apache Spark: Data joins, transformation and filtering the Opportunity Insights Economic Tracker (https://github.com/OpportunityInsights/EconomicTracker)

Jupyter Notebook: Data preprocessing, analysis and visualizations

Plotly and Seaborn: Visualization using a Choropleth map for states and counties and visualize COVID-19 features and impact on the USA states using scatterplots to show correlations 

Colorbrewer 2.0: Information design technique of using sequential color hues within the Choropleth heatmap to represent distinctions within the
colorspace as it relates to the values being visualized
