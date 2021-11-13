# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str#return if yes
  return "Is" + str#return if no

print(new_string("Dense"))
print(new_string("IsHollow"))


