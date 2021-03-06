import numpy as np

import infrastructure.intake as intake
import infrastructure.log as log

import core.topology as topology
import core.satisfaction as satisfaction


def run(graph, img):
    graph = topology.simplify_junctures(graph)
    log.hsvOrGreyImage(img,
        points=(node for node in graph.nodes() if graph.degree(node) != 2)
    )

    graph = topology.simplify_paths(graph)
    log.hsvOrGreyImage(img,
        points=graph.nodes(),
        lines=graph.edges()
    )

    graph = topology.hv_lines(graph)
    log.hsvOrGreyImage(img,
        points=graph.nodes(),
        lines=graph.edges()
    )

    graph = satisfaction.align(graph)
    log.hsvOrGreyImage(img,
        points=graph.nodes(),
        lines=graph.edges()
    )

    return graph


def sample():
    return intake.gpickle("input/grid_graph.gpickle")
