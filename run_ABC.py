import os


if __name__ == "__main__":
    from argparse import ArgumentParser

    print("Start training..")

    parser = ArgumentParser()
    parser.add_argument("--steps", type=int, default=100)
    parser.add_argument("--bs", type=int, default=16)
    args = parser.parse_args()
    result = os.system(
        f"lightweight-gan --data /datastores/pokemon-jpg --num-train-steps {args.steps} --batch-size {args.bs}"
    )
    print(f"Success!: {result}")
