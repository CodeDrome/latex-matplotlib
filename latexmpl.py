import numpy as np
import matplotlib.pyplot as plt


def main():
 
    # squares()

    # sines()

    squareroots()


def squares():

    x = np.linspace(-64,64,129)
    y = x**2

    plt.plot(x,
             y,
             # caret for superscript
             label='$y=x^2$',
             linestyle="-",
             linewidth=0.5,
             color='#0000FF')

    plt.xlabel("$x\\in \\mathbb{R}$")
    plt.ylabel("$y=x^2$")
    # \in and \mathbb{R}
    plt.title("Graph of $f(x)=x^2, x\\in \\mathbb{R}$")
    plt.legend()
    plt.grid(True)

    plt.show()


def sines():
 
    radians = np.linspace(0,2*np.pi,180)
    sinradians = np.sin(radians)

    plt.plot(radians,
             sinradians,
             # \sin and \theta
             label='$y=\\sin \\Theta$',
             linestyle="-",
             linewidth=0.5,
             color='#0000FF')

    plt.xlabel("$\\Theta$")
    plt.ylabel("$\\sin \\Theta$")
    plt.title("Graph of $f(\\Theta)=\\sin \\Theta $")
    plt.legend()
    plt.grid(True)

    plt.show()


def squareroots():

    squares = np.arange(0, 36)
    sqrts = squares**0.5
    
    plt.plot(squares,
             sqrts,
             # \frac{numerator}{denominator}
             label='$y=x^\\frac{1}{2}$',
             linestyle="",
             marker=".",
             linewidth=0.5,
             color='#0000FF')

    plt.xlabel("$x$")
    plt.ylabel("$y=x^\\frac{1}{2}$")
    plt.title("Graph of $f(x)= x^\\frac{1}{2} $")
    plt.legend()
    plt.grid(True)

    plt.show()


if __name__ == "__main__":

    main()