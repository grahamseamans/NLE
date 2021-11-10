import gym
import nle
import tensorflow

def main():
	print("hello world.")

	env = gym.make("NetHackScore-v0")
	env.reset()

	print("This is our action space.")
	print(env.action_space)
	print("This is our observation space.")
	print(env.observation_space)

	print("\nNow running 1000 random actions.")
	for _ in range(1000):
		env.step(env.action_space.sample()) # take a rando action
		# if _ % 50 == 0:
			# env.render()
	print("Printing the rendered environment.")
	env.render()
	env.close()

if __name__ == "__main__":
	main()