"""
http://www.geeksforgeeks.org/compare-two-strings-represented-as-linked-lists/
"""
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents


def compare_two_string_linked_list(lista, listb):
	if not lista or not listb:
		return None
	while lista and listb and lista.contents == listb.contents:
		lista = lista.next
		listb = listb.next

	if lista and listb:
		return 1 if (lista.contents>listb.contents) else -1
	if lista and not listb: return 1
	if listb and not lista: return -1
	return 0

def test_case_one():
	lista = generate_linked_list_with_values(['g', 'e', 'e', 'k', 's', 'a'])
	listb = generate_linked_list_with_values(['g', 'e', 'e', 'k', 's', 'b'])
	return lista, listb

def test_case_two():
	lista = generate_linked_list_with_values(['g', 'e', 'e', 'k', 's'])
	listb = generate_linked_list_with_values(['g', 'e', 'e', 'k', 's'])
	return lista, listb

def test_case_three():
	lista = generate_linked_list_with_values(['g', 'e', 'e', 'k', 's', 'a'])
	listb = generate_linked_list_with_values(['g', 'e', 'e', 'k', 's'])
	return lista, listb

def test_case_four():
	lista = generate_linked_list_with_values(['e', 'e', 'e', 'k', 's', 'a'])
	listb = generate_linked_list_with_values(['g', 'e', 'e', 'k', 's'])
	return lista, listb



def format_output(lista, listb):
	print "---------------"
	print "lista : "
	print_linked_list_contents(lista)
	print "\nlistb : "
	print_linked_list_contents(listb)
	print "\ncomparing two lists : "
	print compare_two_string_linked_list(lista, listb)
	print "---------------"


if __name__ == "__main__":
	head1, head2 = test_case_one()
	print "test_case_one "
	format_output(head1, head2)
	head1, head2 = test_case_two()
	print "test_case_two "
	format_output(head1, head2)
	head1, head2 = test_case_three()
	print "test_case_three"
	format_output(head1, head2)
	head1, head2 = test_case_four()
	print "test_case_four"
	format_output(head1, head2)


