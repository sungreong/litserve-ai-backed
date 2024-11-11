import time
import litserve as ls


class SimpleLogger(ls.Logger):
    def process(self, key, value):
        print(f"Received {key} with value {value}", flush=True)


class PredictionTimeLogger(ls.Callback):
    def on_before_predict(self, lit_api):
        t0 = time.perf_counter()
        self._start_time = t0

    def on_after_predict(self, lit_api):
        t1 = time.perf_counter()
        elapsed = t1 - self._start_time
        lit_api.log("prediction_time", elapsed)
