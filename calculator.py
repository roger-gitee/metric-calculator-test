
class MetricCalculator:
    def __init__(self):
        self.results = []
    
    def calculate_mean(self, data):
        
        if not data:
            return 0.0
        return sum(data) / len(data)
    
    def calculate_accuracy(self, y_true, y_pred):
        
        if not y_true or not y_pred:
            return 0.0
        
        length = min(len(y_true), len(y_pred))
        if length == 0:
            return 0.0
            
        correct = sum(1 for t, p in zip(y_true[:length], y_pred[:length]) if t == p)
        return correct / length
    
    def add_metric(self, name, value):
        self.results.append((name, value))
    
    def get_results(self):
        return self.results