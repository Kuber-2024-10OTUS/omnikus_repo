import kopf
import logging
import kubernetes

@kopf.on.create('epherlvoplumeclaims')
def create_fn(body, **kwargs):
    logging.info(f"A handler is called with body: {body}")