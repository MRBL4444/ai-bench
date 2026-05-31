class Metrics:

    def __init__(self):
        self.rows = []

    def log_task(
        self,
        task_id,
        a_success,
        b_success,
        a_latency,
        b_latency
    ):
        self.rows.append({
            "task_id": task_id,
            "a_success": a_success,
            "b_success": b_success,
            "a_latency": a_latency,
            "b_latency": b_latency
        })

    def summary(self):

        n = len(self.rows)

        if n == 0:
            return {}

        return {
            "A": {
                "success_rate":
                    sum(x["a_success"] for x in self.rows) / n,
                "avg_latency":
                    sum(x["a_latency"] for x in self.rows) / n
            },
            "B": {
                "success_rate":
                    sum(x["b_success"] for x in self.rows) / n,
                "avg_latency":
                    sum(x["b_latency"] for x in self.rows) / n
            }
        }