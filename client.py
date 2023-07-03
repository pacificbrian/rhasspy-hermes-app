# work in progress, add to rhasspy-hermes
def stop_messages(self):
        """Stop receiving future messages from MQTT."""
        try:
            # Handle message in event loop
            if self.loop:
                if self.in_queue:
                    self.loop.call_soon_threadsafe(self.in_queue.put_nowait, None)
                self.loop.stop()
        except Exception:
            self.logger.exception("stop_messages")
