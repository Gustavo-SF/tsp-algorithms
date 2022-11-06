from setuptools.extension import Extension


custom_extension = Extension(
    'tsp_algorithms.ctsp',
    sources=['tsp_algorithms/lib/tsp.c', 'tsp_algorithms/lib/nearest_neighbors.c'],
)


def build(setup_kwargs):
    """
    This is a callback for poetry used to hook in our extensions.
    """

    setup_kwargs.update(
        {
            # declare the extension so that setuptools will compile it
            "ext_modules": [custom_extension],
        }
    )