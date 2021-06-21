courses = ['History', 'Maths', 'Physics', 'CompSci']
#             0           1           2           3
#            -4          -3          -2          -1

print(courses[3] == courses[-1])

print(courses[::-1])  # or
courses.reverse()
# reversing the list.

print(courses[-4:4])

courses.append("Polity")

courses.insert(2, "Arts")

courses_2 = 'P.E.', 'I.T.'

courses.insert(4, courses_2)
# List Within A List.

courses.extend(courses_2)
# individual items get added to the list.

courses.remove("Polity")

print(courses.pop())
# removes the last element from the list, used when we use list as stack or queue.

courses.sort()  # ascending OR
courses.sort(reverse=True)  # Descending

sorted_course = sorted(courses)
print(sorted_course)
