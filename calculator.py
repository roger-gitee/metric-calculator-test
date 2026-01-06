
class MetricCalculator:
    def __init__(self):

        self.results = []
    
    def calculate_mean(self, data):
        
    # ==================== 边界检查层 ====================
    # 检查是否为空列表：防止后续除零错误
    # 如果输入为空，直接返回 0.0 而非抛出异常
        if not data:
            return 0.0
        return sum(data) / len(data)
    
    def calculate_accuracy(self, y_true, y_pred):

    # ==================== 输入验证层 ====================
    # 检查是否任一列表为空：无法计算准确率，返回 0.0   
        
        if not y_true or not y_pred:
            return 0.0
    # ==================== 边界处理层 ====================
    # 统一两个列表的长度：取最小长度，避免索引越界
    # 当长度不一致时，只比较能配对的部分   
        length = min(len(y_true), len(y_pred))
     
    # 检查统一后的长度是否为0（两个列表都为空）
    # 防止后续除零错误    
        if length == 0:
            return 0.0
    # ==================== 核心计算层 ====================
    # 计算正确预测的数量
    # 只比较前 length 个元素，使用 zip 配对
    # 对每一对 (t, p)，如果相等则计数为1，否则为0，最后求和    
        
        correct = sum(1 for t, p in zip(y_true[:length], y_pred[:length]) if t == p)
        return correct / length
    
    def add_metric(self, name, value):

    # 将指标名称和值作为元组添加到结果列表
    # 格式：(name, value)，便于后续检索    
        self.results.append((name, value))
    
    def get_results(self):
        return self.results