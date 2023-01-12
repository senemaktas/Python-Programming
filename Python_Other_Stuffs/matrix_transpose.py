whole_template_result = [ [['wide', 'narrow', 'narrow', 'wide'], ['narrow', 'wide', 'narrow', 'narrow'], ['narrow', 'narrow', 'narrow', 'narrow'],
                         ['wide', 'wide', 'narrow', 'narrow'], ['wide', 'wide', 'narrow', 'narrow']],\

                        [['wide', 'wide', 'narrow', 'wide'], ['narrow', 'wide', 'narrow', 'narrow'], ['narrow', 'wide', 'narrow', 'narrow'],
                         ['wide', 'wide', 'wide', 'narrow'], ['wide', 'narrow', 'wide', 'wide']],\

                        [['narrow', 'narrow', 'narrow', 'narrow'], ['wide', 'wide', 'narrow', 'narrow'], ['wide', 'wide', 'narrow', 'narrow'],
                         ['wide', 'narrow', 'narrow', 'wide'], ['wide', 'narrow', 'narrow', 'narrow']]]

from collections import Counter

whole_template_result_trans = list(zip(*whole_template_result))
analysis_result = []
for i , one_shoot in enumerate(whole_template_result_trans):
    template_result_trans = list(zip(*one_shoot))

    template_last_result = []
    for j, each_pair_val in enumerate(template_result_trans):

        counter_object = Counter(template_result_trans[j])
        max_val = max(counter_object, key=counter_object.get)
        template_last_result.append(max_val)
    analysis_result.append(template_last_result)

print(analysis_result)