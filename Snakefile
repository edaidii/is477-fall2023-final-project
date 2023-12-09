rule prepare:
  output:
    "data/car+evaluation/car.csv"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input: 
    "data/car+evaluation/car.csv"
  output:
    "profiling/profiling.html"
  shell:
    "python scripts/profile.py"

rule analyze:
  input:
    "data/car+evaluation/car.csv"
  output:
    "results/summary_stats.csv",
    "results/maintenance_class_value_distribution.csv",
    "results/maintenance_cost_class_value.png"
  shell:
  "python scripts/analysis.py"