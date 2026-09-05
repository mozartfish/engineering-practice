import numpy as np


class MLP:
    def __init__(self, num_inputs=3, num_hidden=[3, 5], num_outputs=2, debug=False):
        """
        Args:
            num_inputs - number of neurons in input layer
            num_hidden - list containing integers. each integer represents the number of neurons in a hidden layer
            num_outputs - number of neurons in output layer
        """
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs

        # internal representation of the layers
        # each number represents the number of neurons in a layer
        layers = [self.num_inputs] + self.num_hidden + [self.num_outputs]
        if debug:
            print(f"number of neurons in each layer: {layers}")

        # initiate random weights
        self.weights = []
        for i in range(len(layers) - 1):
            # w - matrix whose dimensions are the number of neurons in the current layer x number of neurons in the next
            # layer for matrix multiplication
            w = np.random.rand(layers[i], layers[i + 1])
            self.weights.append(w)

    def forward_propagate(self, inputs):
        """
        Computes forward propagation of the network based on input signals
        Args:
            inputs: input signals
        Returns:
            activations: output values
        """
        activations = inputs
        for w in self.weights:
            # calculate net inputs(h) for a given layer
            net_inputs = activations @ w

            # calculate the activations(a) for a given layer
            activations = self._sigmoid(net_inputs)

        return activations

    def _sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))


if __name__ == "__main__":
    # create multi-layer-perceptron
    mlp = MLP()

    # create inputs
    inputs = np.random.rand(mlp.num_inputs)

    # perform forward propagation
    outputs = mlp.forward_propagate(inputs)

    # print results
    print(f"network inputs: {inputs} | network outputs: {outputs}")
