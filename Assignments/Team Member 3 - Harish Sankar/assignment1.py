{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Basic Python"
      ],
      "metadata": {
        "id": "McSxJAwcOdZ1"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 1. Split this string"
      ],
      "metadata": {
        "id": "CU48hgo4Owz5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "s = \"Hi there Sam!\""
      ],
      "metadata": {
        "id": "s07c7JK7Oqt-"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(s.split())"
      ],
      "metadata": {
        "id": "6mGVa3SQYLkb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "88d899a7-0e82-4c51-80fe-8b1ec32634fb"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hi', 'there', 'Sam!']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 2. Use .format() to print the following string. \n",
        "\n",
        "### Output should be: The diameter of Earth is 12742 kilometers."
      ],
      "metadata": {
        "id": "GH1QBn8HP375"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "planet = \"Earth\"\n",
        "diameter = 12742"
      ],
      "metadata": {
        "id": "_ZHoml3kPqic"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"The diameter of {planet} is {diameter} kilometers.\")"
      ],
      "metadata": {
        "id": "HyRyJv6CYPb4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "31f5550d-7686-49ea-e416-dcd3dce7ab72"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The diameter of Earth is 12742 kilometers.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 3. In this nest dictionary grab the word \"hello\""
      ],
      "metadata": {
        "id": "KE74ZEwkRExZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}"
      ],
      "metadata": {
        "id": "fcVwbCc1QrQI"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(d['k1'][3]['tricky'][3]['target'][3])"
      ],
      "metadata": {
        "id": "MvbkMZpXYRaw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "28a1f469-0544-4135-c069-95c2cac23fc2"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Numpy"
      ],
      "metadata": {
        "id": "bw0vVp-9ddjv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "LLiE_TYrhA1O"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 4.1 Create an array of 10 zeros? \n",
        "## 4.2 Create an array of 10 fives?"
      ],
      "metadata": {
        "id": "wOg8hinbgx30"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "array = np.zeros(10)\n",
        "print(\"An array of 10 zeros:\")\n",
        "print(array)"
      ],
      "metadata": {
        "id": "NHrirmgCYXvU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b8556ace-2dab-4060-8331-eeccdb0badf3"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "An array of 10 zeros:\n",
            "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "array = np.ones(10)*5\n",
        "print(\"An array of 10 fives:\")\n",
        "print(array)"
      ],
      "metadata": {
        "id": "e4005lsTYXxx",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1a52e3d2-e0ec-46fe-a9b6-0590124d81c5"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "An array of 10 fives:\n",
            "[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 5. Create an array of all the even integers from 20 to 35"
      ],
      "metadata": {
        "id": "gZHHDUBvrMX4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "array = np.empty(0)\n",
        "for i in range(20, 35):\n",
        "  if (i % 2 == 0):\n",
        "    print(i, end = ' ')\n",
        "    np.append(array, [i])"
      ],
      "metadata": {
        "id": "oAI2tbU2Yag-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "10e7f94c-8d5b-45a6-977c-3283d43e8929"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20 22 24 26 28 30 32 34 "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 6. Create a 3x3 matrix with values ranging from 0 to 8"
      ],
      "metadata": {
        "id": "NaOM308NsRpZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a =  np.arange(0, 9).reshape(3,3)\n",
        "print(a)"
      ],
      "metadata": {
        "id": "tOlEVH7BYceE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "442ddb3d-b10d-4285-a802-b5ed256a2541"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[0 1 2]\n",
            " [3 4 5]\n",
            " [6 7 8]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 7. Concatenate a and b \n",
        "## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])"
      ],
      "metadata": {
        "id": "hQ0dnhAQuU_p"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = np.array([[1, 2, 3]])\n",
        "b = np.array([[4, 5, 6]])\n",
        "result = np.concatenate((a, b), axis=0)\n",
        "print(result)"
      ],
      "metadata": {
        "id": "rAPSw97aYfE0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bbaa8899-128b-4c3a-f789-c978b3b1be07"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2 3]\n",
            " [4 5 6]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Pandas"
      ],
      "metadata": {
        "id": "dlPEY9DRwZga"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 8. Create a dataframe with 3 rows and 2 columns"
      ],
      "metadata": {
        "id": "ijoYW51zwr87"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n"
      ],
      "metadata": {
        "id": "T5OxJRZ8uvR7"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data = [[0, 1], [1, 0], [1, 1]]\n",
        "df = pd.DataFrame(data, columns=['A','B'])\n",
        "print(df)"
      ],
      "metadata": {
        "id": "xNpI_XXoYhs0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5704c2ad-91c3-49f8-8b00-e6cf8b85579d"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   A  B\n",
            "0  0  1\n",
            "1  1  0\n",
            "2  1  1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"
      ],
      "metadata": {
        "id": "UXSmdNclyJQD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "date = pd.date_range(start ='1-1-2023', end ='2-10-2023')\n",
        "for val in date:\n",
        "    print(val)"
      ],
      "metadata": {
        "id": "dgyC0JhVYl4F",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5f186180-9d38-4e22-f4bb-e92f60b16e19"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2023-01-01 00:00:00\n",
            "2023-01-02 00:00:00\n",
            "2023-01-03 00:00:00\n",
            "2023-01-04 00:00:00\n",
            "2023-01-05 00:00:00\n",
            "2023-01-06 00:00:00\n",
            "2023-01-07 00:00:00\n",
            "2023-01-08 00:00:00\n",
            "2023-01-09 00:00:00\n",
            "2023-01-10 00:00:00\n",
            "2023-01-11 00:00:00\n",
            "2023-01-12 00:00:00\n",
            "2023-01-13 00:00:00\n",
            "2023-01-14 00:00:00\n",
            "2023-01-15 00:00:00\n",
            "2023-01-16 00:00:00\n",
            "2023-01-17 00:00:00\n",
            "2023-01-18 00:00:00\n",
            "2023-01-19 00:00:00\n",
            "2023-01-20 00:00:00\n",
            "2023-01-21 00:00:00\n",
            "2023-01-22 00:00:00\n",
            "2023-01-23 00:00:00\n",
            "2023-01-24 00:00:00\n",
            "2023-01-25 00:00:00\n",
            "2023-01-26 00:00:00\n",
            "2023-01-27 00:00:00\n",
            "2023-01-28 00:00:00\n",
            "2023-01-29 00:00:00\n",
            "2023-01-30 00:00:00\n",
            "2023-01-31 00:00:00\n",
            "2023-02-01 00:00:00\n",
            "2023-02-02 00:00:00\n",
            "2023-02-03 00:00:00\n",
            "2023-02-04 00:00:00\n",
            "2023-02-05 00:00:00\n",
            "2023-02-06 00:00:00\n",
            "2023-02-07 00:00:00\n",
            "2023-02-08 00:00:00\n",
            "2023-02-09 00:00:00\n",
            "2023-02-10 00:00:00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 10. Create 2D list to DataFrame\n",
        "\n",
        "lists = [[1, 'aaa', 22],\n",
        "         [2, 'bbb', 25],\n",
        "         [3, 'ccc', 24]]"
      ],
      "metadata": {
        "id": "ZizSetD-y5az"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]"
      ],
      "metadata": {
        "id": "_XMC8aEt0llB"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.DataFrame(lists)\n",
        "print(df)"
      ],
      "metadata": {
        "id": "knH76sDKYsVX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5e1ae454-ad3d-4a6e-ba74-e8792d3b734a"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   0    1   2\n",
            "0  1  aaa  22\n",
            "1  2  bbb  25\n",
            "2  3  ccc  24\n"
          ]
        }
      ]
    }
  ]
}
